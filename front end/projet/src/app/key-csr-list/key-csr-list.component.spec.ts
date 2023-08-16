import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KeyCSRListComponent } from './key-csr-list.component';

describe('KeyCSRListComponent', () => {
  let component: KeyCSRListComponent;
  let fixture: ComponentFixture<KeyCSRListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ KeyCSRListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KeyCSRListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
