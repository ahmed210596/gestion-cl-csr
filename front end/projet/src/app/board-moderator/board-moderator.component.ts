import { Component, OnInit, AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { UserService } from '../user.service';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-board-moderator',
  templateUrl: './board-moderator.component.html',
  styleUrls: ['./board-moderator.component.css']
})
export class BoardModeratorComponent implements OnInit {
  @ViewChild('barChart', { static: false }) barChart!: ElementRef;
  @ViewChild('pieChart', { static: false }) pieChart!: ElementRef;

  content?: string;
  employerBoardData: any;
  error?: string;
  chart:any;
  prod: any;

  constructor(private userService: UserService) {
    //this.employerBoardData = {};
  }

 

  ngOnInit(): void {
    this.userService.getModeratorBoard().subscribe(
      (data) => {
        this.employerBoardData = data;
        this.prod = data.products_created;
        console.log(this.employerBoardData);
        console.log(data)
        this.renderChart(data)
      },
      (error) => {
        this.error = error.message;
      }
    );
  }
  renderChart(data: any) {
    const ctx = document.getElementById('myChart') as HTMLCanvasElement;
    this.chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Total Products', 'Total Serials', 'Products Created', 'Serials Created'],
        datasets: [
          {
            label: 'Employer Dashboard',
            data: [
              data.total_products,
              data.total_serials,
              data.products_created,
              data.serials_created
            ],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
              'rgba(255,99,132,1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
          }
        ]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }

  

  
}



