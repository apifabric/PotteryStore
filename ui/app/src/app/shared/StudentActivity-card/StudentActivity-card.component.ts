import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './StudentActivity-card.component.html',
  styleUrls: ['./StudentActivity-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.StudentActivity-card]': 'true'
  }
})

export class StudentActivityCardComponent {


}