import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrderReportHomeComponent } from './home/OrderReport-home.component';
import { OrderReportNewComponent } from './new/OrderReport-new.component';
import { OrderReportDetailComponent } from './detail/OrderReport-detail.component';

const routes: Routes = [
  {path: '', component: OrderReportHomeComponent},
  { path: 'new', component: OrderReportNewComponent },
  { path: ':id', component: OrderReportDetailComponent,
    data: {
      oPermission: {
        permissionId: 'OrderReport-detail-permissions'
      }
    }
  }
];

export const ORDERREPORT_MODULE_DECLARATIONS = [
    OrderReportHomeComponent,
    OrderReportNewComponent,
    OrderReportDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class OrderReportRoutingModule { }