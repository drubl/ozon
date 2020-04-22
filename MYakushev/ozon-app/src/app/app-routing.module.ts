import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PageCartComponent } from './page-cart/page-cart.component';
import { PageSearchComponent } from './page-search/page-search.component';
import { PageProductComponent} from './page-product/page-product.component';
import { PageCustomerComponent} from './page-customer/page-customer.component';

const routes: Routes = [
  { path: '', redirectTo: '/search', pathMatch: 'full' },
  { path: 'cart', component: PageCartComponent },
  { path: 'search', component: PageSearchComponent },
  { path: 'products/: id', component: PageProductComponent },
  { path: 'customer', component: PageCustomerComponent }
];

@NgModule({
  exports: [ RouterModule ],
  imports: [ RouterModule.forRoot(routes) ],
})
export class AppRoutingModule {}
