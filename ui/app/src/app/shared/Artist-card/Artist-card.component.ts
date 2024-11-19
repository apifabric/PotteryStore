import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Artist-card.component.html',
  styleUrls: ['./Artist-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Artist-card]': 'true'
  }
})

export class ArtistCardComponent {


}