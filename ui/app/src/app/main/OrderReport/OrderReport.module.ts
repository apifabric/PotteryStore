import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ORDERREPORT_MODULE_DECLARATIONS, OrderReportRoutingModule} from  './OrderReport-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    OrderReportRoutingModule
  ],
  declarations: ORDERREPORT_MODULE_DECLARATIONS,
  exports: ORDERREPORT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class OrderReportModule { }