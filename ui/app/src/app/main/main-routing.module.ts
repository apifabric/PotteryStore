import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Activity', loadChildren: () => import('./Activity/Activity.module').then(m => m.ActivityModule) },
    
        { path: 'Artist', loadChildren: () => import('./Artist/Artist.module').then(m => m.ArtistModule) },
    
        { path: 'Class', loadChildren: () => import('./Class/Class.module').then(m => m.ClassModule) },
    
        { path: 'ClassReport', loadChildren: () => import('./ClassReport/ClassReport.module').then(m => m.ClassReportModule) },
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Enrollment', loadChildren: () => import('./Enrollment/Enrollment.module').then(m => m.EnrollmentModule) },
    
        { path: 'Item', loadChildren: () => import('./Item/Item.module').then(m => m.ItemModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'OrderDetail', loadChildren: () => import('./OrderDetail/OrderDetail.module').then(m => m.OrderDetailModule) },
    
        { path: 'OrderReport', loadChildren: () => import('./OrderReport/OrderReport.module').then(m => m.OrderReportModule) },
    
        { path: 'Student', loadChildren: () => import('./Student/Student.module').then(m => m.StudentModule) },
    
        { path: 'StudentActivity', loadChildren: () => import('./StudentActivity/StudentActivity.module').then(m => m.StudentActivityModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }