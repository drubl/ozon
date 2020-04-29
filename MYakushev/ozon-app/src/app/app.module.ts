import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { CustomerPageComponent } from './customer-page/customer-page.component';
import { CartPageComponent } from './cart-page/cart-page.component';
import { ProductPageComponent } from './product-page/product-page.component';
import { HeaderComponent } from './shared/components/header/header.component';
import { ProductComponent } from './shared/components/product/product.component';
import { MainLayoutComponent } from './shared/components/main-layout/main-layout.component';
import { CategoryPageComponent } from './category-page/category-page.component';
import { HomePageComponent } from './home-page/home-page.component';
import { LogoComponent } from './shared/components/header/logo/logo.component';
import { SearchFormComponent } from './shared/components/header/search-form/search-form.component';
import { NavCustomerComponent } from './shared/components/header/nav-customer/nav-customer.component';
import { NavCategoryComponent } from './shared/components/header/nav-category/nav-category.component';
import { ModalWindowComponent } from './shared/components/modal-window/modal-window.component';
import { ModalPageSignInComponent } from './shared/components/modal-window/modal-page-sign-in/modal-page-sign-in.component';
import { ModalPageRegComponent } from './shared/components/modal-window/modal-page-reg/modal-page-reg.component';
import { ModalPageCartComponent } from './shared/components/modal-window/modal-page-cart/modal-page-cart.component';
import { ModalPageCustomerComponent } from './shared/components/modal-window/modal-page-customer/modal-page-customer.component';
import { ModalPageCategoryComponent } from './shared/components/modal-window/modal-page-category/modal-page-category.component';
import {ReactiveFormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    SearchPageComponent,
    CustomerPageComponent,
    CartPageComponent,
    ProductPageComponent,
    HeaderComponent,
    ProductComponent,
    MainLayoutComponent,
    CategoryPageComponent,
    HomePageComponent,
    LogoComponent,
    SearchFormComponent,
    NavCustomerComponent,
    NavCategoryComponent,
    ModalWindowComponent,
    ModalPageSignInComponent,
    ModalPageRegComponent,
    ModalPageCartComponent,
    ModalPageCustomerComponent,
    ModalPageCategoryComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        ReactiveFormsModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
