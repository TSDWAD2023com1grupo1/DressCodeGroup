import { TestBed } from '@angular/core/testing';

import { UsuarioService } from './Usuario.service';

describe('ServicioBackService', () => {
  let service: UsuarioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UsuarioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
