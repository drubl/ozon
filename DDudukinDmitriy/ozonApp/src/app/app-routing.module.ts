import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {ProfilePageComponent} from './pages/profile-page/profile-page.component';
import {SearchPageComponent} from './pages/search-page/search-page.component';
import {ShoppingCartComponent} from './pages/shopping-cart/shopping-cart.component';
import {ProductInformationComponent} from './pages/product-information/product-information.component'
import {HomePageComponent} from "./pages/home-page/home-page.component";


const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'shoppingCart', component: ShoppingCartComponent},
  {path: 'profile', component: ProfilePageComponent},
  {path: 'product', component: SearchPageComponent},
  {path: 'product/:id', component: ProductInformationComponent},
  {path: 'home', component: HomePageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
