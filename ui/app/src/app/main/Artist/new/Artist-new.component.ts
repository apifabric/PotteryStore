import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Artist-new',
  templateUrl: './Artist-new.component.html',
  styleUrls: ['./Artist-new.component.scss']
})
export class ArtistNewComponent {
  @ViewChild("ArtistForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}