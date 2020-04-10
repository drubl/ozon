import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PageCartComponent } from './page-cart/page-cart.component';
import { PageMainComponent } from './page-main/page-main.component';
import { PageProductComponent} from './page-product/page-product.component';
import { PageCustomerComponent} from './page-customer/page-customer.component';

const routes: Routes = [
  { path: '', redirectTo: '/product', pathMatch: 'full' },
  { path: 'cart', component: PageCartComponent },
  { path: 'product', component: PageMainComponent },
  { path: 'single-product', component: PageProductComponent },
  { path: 'customer', component: PageCustomerComponent }
];

@NgModule({
  exports: [ RouterModule ],
  imports: [ RouterModule.forRoot(routes) ],
})
export class AppRoutingModule {}
