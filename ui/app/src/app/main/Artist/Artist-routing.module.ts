import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ArtistHomeComponent } from './home/Artist-home.component';
import { ArtistNewComponent } from './new/Artist-new.component';
import { ArtistDetailComponent } from './detail/Artist-detail.component';

const routes: Routes = [
  {path: '', component: ArtistHomeComponent},
  { path: 'new', component: ArtistNewComponent },
  { path: ':id', component: ArtistDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Artist-detail-permissions'
      }
    }
  },{
    path: ':artist_id/Class', loadChildren: () => import('../Class/Class.module').then(m => m.ClassModule),
    data: {
        oPermission: {
            permissionId: 'Class-detail-permissions'
        }
    }
},{
    path: ':artist_id/Item', loadChildren: () => import('../Item/Item.module').then(m => m.ItemModule),
    data: {
        oPermission: {
            permissionId: 'Item-detail-permissions'
        }
    }
}
];

export const ARTIST_MODULE_DECLARATIONS = [
    ArtistHomeComponent,
    ArtistNewComponent,
    ArtistDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ArtistRoutingModule { }