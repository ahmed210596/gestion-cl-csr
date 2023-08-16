import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteDialogSerialComponent } from './delete-dialog-serial.component';

describe('DeleteDialogSerialComponent', () => {
  let component: DeleteDialogSerialComponent;
  let fixture: ComponentFixture<DeleteDialogSerialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteDialogSerialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteDialogSerialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
