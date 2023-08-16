import { TestBed } from '@angular/core/testing';

import { KeycsrService } from './keycsr.service';

describe('KeycsrService', () => {
  let service: KeycsrService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KeycsrService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
