import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Class-card.component.html',
  styleUrls: ['./Class-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Class-card]': 'true'
  }
})

export class ClassCardComponent {


}