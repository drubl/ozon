import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { SearchFormComponent } from './header/common/search-form/search-form.component';
import { ProductCardComponent } from './product-card/product-card.component';
import { ProfilePageComponent } from './profile-page/profile-page.component';
import { ProductInformationComponent } from './product-information/product-information.component';
import { ProfileSideBarComponent } from './profile-page/common/profile-side-bar/profile-side-bar.component';
import { ShoppingCartComponent } from './shopping-cart/shopping-cart.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { ShoppingCartProductComponent } from './shopping-cart/common/shopping-cart-product/shopping-cart-product.component';
import { CheckoutComponent } from './shopping-cart/common/checkout/checkout.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    SearchFormComponent,
    ProductCardComponent,
    ProfilePageComponent,
    ProductInformationComponent,
    ProfileSideBarComponent,
    ShoppingCartComponent,
    SearchPageComponent,
    ShoppingCartProductComponent,
    CheckoutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
