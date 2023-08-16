import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditSerialsComponent } from './edit-serials.component';

describe('EditSerialsComponent', () => {
  let component: EditSerialsComponent;
  let fixture: ComponentFixture<EditSerialsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditSerialsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditSerialsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
