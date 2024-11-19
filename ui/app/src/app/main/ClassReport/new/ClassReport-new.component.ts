import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'ClassReport-new',
  templateUrl: './ClassReport-new.component.html',
  styleUrls: ['./ClassReport-new.component.scss']
})
export class ClassReportNewComponent {
  @ViewChild("ClassReportForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}