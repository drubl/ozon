import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProfilePageComponent } from './profile-page/profile-page.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { ShoppingCartComponent } from './shopping-cart/shopping-cart.component';
import { ProductInformationComponent } from './pages/product-information/product-information.component'



const routes: Routes = [
  { path: '', redirectTo: 'product', pathMatch: 'full' },
  { path: 'shoppingCart', component: ShoppingCartComponent },
  { path: 'profile', component: ProfilePageComponent },
  { path: 'product', component: SearchPageComponent },
  { path: 'product/:id', component: ProductInformationComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
