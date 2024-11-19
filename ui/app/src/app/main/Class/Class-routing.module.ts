import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClassHomeComponent } from './home/Class-home.component';
import { ClassNewComponent } from './new/Class-new.component';
import { ClassDetailComponent } from './detail/Class-detail.component';

const routes: Routes = [
  {path: '', component: ClassHomeComponent},
  { path: 'new', component: ClassNewComponent },
  { path: ':id', component: ClassDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Class-detail-permissions'
      }
    }
  }
];

export const CLASS_MODULE_DECLARATIONS = [
    ClassHomeComponent,
    ClassNewComponent,
    ClassDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ClassRoutingModule { }