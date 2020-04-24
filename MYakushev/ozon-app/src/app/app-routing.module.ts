import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PageCartComponent } from './pages/page-cart/page-cart.component';
import { PageSearchComponent } from './pages/page-search/page-search.component';
import { PageProductComponent} from './pages/page-product/page-product.component';
import { PageCustomerComponent} from './pages/page-customer/page-customer.component';
import {PageRegistrationComponent} from './pages/page-registration/page-registration.component';

const routes: Routes = [
  { path: '', redirectTo: '/search', pathMatch: 'full' },
  { path: 'cart', component: PageCartComponent },
  { path: 'registration', component: PageRegistrationComponent },
  { path: 'search', component: PageSearchComponent },
  { path: 'products/: id', component: PageProductComponent },
  { path: 'customer', component: PageCustomerComponent }
];

@NgModule({
  exports: [ RouterModule ],
  imports: [ RouterModule.forRoot(routes) ],
})
export class AppRoutingModule {}
