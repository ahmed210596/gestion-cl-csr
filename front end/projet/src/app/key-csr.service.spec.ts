import { TestBed } from '@angular/core/testing';

import { KeyCSRService } from './key-csr.service';

describe('KeyCSRService', () => {
  let service: KeyCSRService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KeyCSRService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
