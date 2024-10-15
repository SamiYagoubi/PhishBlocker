import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalysResultComponent } from './analys-result.component';

describe('AnalysResultComponent', () => {
  let component: AnalysResultComponent;
  let fixture: ComponentFixture<AnalysResultComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AnalysResultComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AnalysResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
