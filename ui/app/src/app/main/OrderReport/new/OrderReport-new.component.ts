import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'OrderReport-new',
  templateUrl: './OrderReport-new.component.html',
  styleUrls: ['./OrderReport-new.component.scss']
})
export class OrderReportNewComponent {
  @ViewChild("OrderReportForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}