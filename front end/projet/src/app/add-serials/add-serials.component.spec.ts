import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddSerialsComponent } from './add-serials.component';

describe('AddSerialsComponent', () => {
  let component: AddSerialsComponent;
  let fixture: ComponentFixture<AddSerialsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddSerialsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddSerialsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
