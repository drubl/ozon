import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {MainLayoutComponent} from './shared/components/main-layout/main-layout.component';
import {CategoryPageComponent} from './category-page/category-page.component';
import {ProductPageComponent} from './product-page/product-page.component';
import {SearchPageComponent} from './search-page/search-page.component';
import {CustomerPageComponent} from './customer-page/customer-page.component';
import {CartPageComponent} from './cart-page/cart-page.component';
import {HomePageComponent} from './home-page/home-page.component';


const routes: Routes = [
  {
    path: '', component: MainLayoutComponent, children: [
      {path: '', redirectTo: '/', pathMatch: 'full'},
      {path: '', component: HomePageComponent},
      {path: 'category', component: CategoryPageComponent},
      {path: 'category/:name', component: CategoryPageComponent},
      {path: 'product/:id', component: ProductPageComponent},
      {path: 'search/:name', component: SearchPageComponent},
      {path: 'customer', component: CustomerPageComponent},
      {path: 'cart', component: CartPageComponent},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
