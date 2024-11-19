import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClassReportHomeComponent } from './home/ClassReport-home.component';
import { ClassReportNewComponent } from './new/ClassReport-new.component';
import { ClassReportDetailComponent } from './detail/ClassReport-detail.component';

const routes: Routes = [
  {path: '', component: ClassReportHomeComponent},
  { path: 'new', component: ClassReportNewComponent },
  { path: ':id', component: ClassReportDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ClassReport-detail-permissions'
      }
    }
  }
];

export const CLASSREPORT_MODULE_DECLARATIONS = [
    ClassReportHomeComponent,
    ClassReportNewComponent,
    ClassReportDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ClassReportRoutingModule { }