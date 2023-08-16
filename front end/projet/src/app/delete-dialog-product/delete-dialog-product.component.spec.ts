import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteDialogProductComponent } from './delete-dialog-product.component';

describe('DeleteDialogProductComponent', () => {
  let component: DeleteDialogProductComponent;
  let fixture: ComponentFixture<DeleteDialogProductComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteDialogProductComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteDialogProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
