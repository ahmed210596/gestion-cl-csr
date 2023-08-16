import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListSerialsComponent } from './list-serials.component';

describe('ListSerialsComponent', () => {
  let component: ListSerialsComponent;
  let fixture: ComponentFixture<ListSerialsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListSerialsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListSerialsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
