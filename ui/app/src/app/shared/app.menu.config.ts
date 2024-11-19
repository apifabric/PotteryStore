import { MenuRootItem } from 'ontimize-web-ngx';

import { ActivityCardComponent } from './Activity-card/Activity-card.component';

import { ArtistCardComponent } from './Artist-card/Artist-card.component';

import { ClassCardComponent } from './Class-card/Class-card.component';

import { ClassReportCardComponent } from './ClassReport-card/ClassReport-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EnrollmentCardComponent } from './Enrollment-card/Enrollment-card.component';

import { ItemCardComponent } from './Item-card/Item-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderDetailCardComponent } from './OrderDetail-card/OrderDetail-card.component';

import { OrderReportCardComponent } from './OrderReport-card/OrderReport-card.component';

import { StudentCardComponent } from './Student-card/Student-card.component';

import { StudentActivityCardComponent } from './StudentActivity-card/StudentActivity-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Activity', name: 'ACTIVITY', icon: 'view_list', route: '/main/Activity' }
    
        ,{ id: 'Artist', name: 'ARTIST', icon: 'view_list', route: '/main/Artist' }
    
        ,{ id: 'Class', name: 'CLASS', icon: 'view_list', route: '/main/Class' }
    
        ,{ id: 'ClassReport', name: 'CLASSREPORT', icon: 'view_list', route: '/main/ClassReport' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Enrollment', name: 'ENROLLMENT', icon: 'view_list', route: '/main/Enrollment' }
    
        ,{ id: 'Item', name: 'ITEM', icon: 'view_list', route: '/main/Item' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderDetail', name: 'ORDERDETAIL', icon: 'view_list', route: '/main/OrderDetail' }
    
        ,{ id: 'OrderReport', name: 'ORDERREPORT', icon: 'view_list', route: '/main/OrderReport' }
    
        ,{ id: 'Student', name: 'STUDENT', icon: 'view_list', route: '/main/Student' }
    
        ,{ id: 'StudentActivity', name: 'STUDENTACTIVITY', icon: 'view_list', route: '/main/StudentActivity' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    ActivityCardComponent

    ,ArtistCardComponent

    ,ClassCardComponent

    ,ClassReportCardComponent

    ,CustomerCardComponent

    ,EnrollmentCardComponent

    ,ItemCardComponent

    ,OrderCardComponent

    ,OrderDetailCardComponent

    ,OrderReportCardComponent

    ,StudentCardComponent

    ,StudentActivityCardComponent

];