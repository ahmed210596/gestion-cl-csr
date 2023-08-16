import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditCsrComponent } from './edit-csr.component';

describe('EditCsrComponent', () => {
  let component: EditCsrComponent;
  let fixture: ComponentFixture<EditCsrComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditCsrComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditCsrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
