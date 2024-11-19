import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CLASSREPORT_MODULE_DECLARATIONS, ClassReportRoutingModule} from  './ClassReport-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ClassReportRoutingModule
  ],
  declarations: CLASSREPORT_MODULE_DECLARATIONS,
  exports: CLASSREPORT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ClassReportModule { }