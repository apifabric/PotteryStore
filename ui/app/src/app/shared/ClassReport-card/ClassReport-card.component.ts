import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './ClassReport-card.component.html',
  styleUrls: ['./ClassReport-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.ClassReport-card]': 'true'
  }
})

export class ClassReportCardComponent {


}