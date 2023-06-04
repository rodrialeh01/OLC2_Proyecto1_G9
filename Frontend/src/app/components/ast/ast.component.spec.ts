import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AstComponent } from './ast.component';

describe('AstComponent', () => {
  let component: AstComponent;
  let fixture: ComponentFixture<AstComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AstComponent]
    });
    fixture = TestBed.createComponent(AstComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
