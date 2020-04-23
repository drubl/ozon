import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { LogoComponent } from './header/logo/logo.component';
import { SearchFormComponent } from './header/search-form/search-form.component';
import { NavCustomerButtonComponent } from './header/nav-customer-button/nav-customer-button.component';
import { PageSearchComponent } from './pages/page-search/page-search.component';
import { ProductItemComponent } from './pages/page-search/product-item/product-item.component';
import { AppRoutingModule } from './app-routing.module';
import { PageCartComponent } from './pages/page-cart/page-cart.component';
import { SelectedProductsComponent } from './pages/page-cart/components/selected-products/selected-products.component';
import { InformationProductsComponent } from './pages/page-cart/components/information-products/information-products.component';
import { PageProductComponent } from './pages/page-product/page-product.component';
import { ProductGalleryComponent } from './pages/page-product/components/product-gallery/product-gallery.component';
import { PageCustomerComponent } from './pages/page-customer/page-customer.component';
import { PriceAndAddCartComponent } from './pages/page-product/components/price-and-add-cart/price-and-add-cart.component';
import { CustomerNavComponent } from './pages/page-customer/components/customer-nav/customer-nav.component';
import { CustomerInfoComponent } from './pages/page-customer/components/customer-info/customer-info.component';
import {HttpClientModule} from "@angular/common/http";
import { ModalWindowComponent } from './header/nav-customer-button/modal-window/modal-window.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { ModalPageSignInComponent } from './header/nav-customer-button/modal-window/pages/modal-page-sign-in/modal-page-sign-in.component';
import { ModalPageRegComponent } from './header/nav-customer-button/modal-window/pages/modal-page-reg/modal-page-reg.component';
import { PageRegistrationComponent } from './pages/page-registration/page-registration.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LogoComponent,
    SearchFormComponent,
    NavCustomerButtonComponent,
    PageSearchComponent,
    ProductItemComponent,
    PageCartComponent,
    SelectedProductsComponent,
    InformationProductsComponent,
    PageProductComponent,
    ProductGalleryComponent,
    PageCustomerComponent,
    PriceAndAddCartComponent,
    CustomerNavComponent,
    CustomerInfoComponent,
    ModalWindowComponent,
    ModalPageSignInComponent,
    ModalPageRegComponent,
    PageRegistrationComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
