import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './OrderReport-card.component.html',
  styleUrls: ['./OrderReport-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.OrderReport-card]': 'true'
  }
})

export class OrderReportCardComponent {


}