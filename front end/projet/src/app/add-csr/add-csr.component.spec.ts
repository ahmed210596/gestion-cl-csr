import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddCsrComponent } from './add-csr.component';

describe('AddCsrComponent', () => {
  let component: AddCsrComponent;
  let fixture: ComponentFixture<AddCsrComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddCsrComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddCsrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
