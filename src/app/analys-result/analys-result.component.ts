import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-analys-result',
  templateUrl: './analys-result.component.html',
  styleUrls: ['./analys-result.component.css']
})
export class AnalysResultComponent implements OnInit {
  result: any;

  constructor(private router: Router) { }

  ngOnInit(): void {
    const navigation = this.router.getCurrentNavigation();
    if (navigation?.extras.state?.['data']) {
      this.result = navigation.extras.state['data'];
    }
  }
}
