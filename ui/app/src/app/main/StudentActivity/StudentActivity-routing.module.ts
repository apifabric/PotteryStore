import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StudentActivityHomeComponent } from './home/StudentActivity-home.component';
import { StudentActivityNewComponent } from './new/StudentActivity-new.component';
import { StudentActivityDetailComponent } from './detail/StudentActivity-detail.component';

const routes: Routes = [
  {path: '', component: StudentActivityHomeComponent},
  { path: 'new', component: StudentActivityNewComponent },
  { path: ':id', component: StudentActivityDetailComponent,
    data: {
      oPermission: {
        permissionId: 'StudentActivity-detail-permissions'
      }
    }
  }
];

export const STUDENTACTIVITY_MODULE_DECLARATIONS = [
    StudentActivityHomeComponent,
    StudentActivityNewComponent,
    StudentActivityDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StudentActivityRoutingModule { }