import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'StudentActivity-new',
  templateUrl: './StudentActivity-new.component.html',
  styleUrls: ['./StudentActivity-new.component.scss']
})
export class StudentActivityNewComponent {
  @ViewChild("StudentActivityForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}