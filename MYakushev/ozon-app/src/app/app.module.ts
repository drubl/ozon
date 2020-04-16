import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { LogoComponent } from './header/logo/logo.component';
import { SearchFormComponent } from './header/search-form/search-form.component';
import { NavCustomerButtonComponent } from './header/nav-customer-button/nav-customer-button.component';
import { PageSearchComponent } from './page-search/page-search.component';
import { ProductItemComponent } from './page-search/product-item/product-item.component';
import { AppRoutingModule } from './app-routing.module';
import { PageCartComponent } from './page-cart/page-cart.component';
import { SelectedProductsComponent } from './page-cart/selected-products/selected-products.component';
import { InformationProductsComponent } from './page-cart/information-products/information-products.component';
import { PageProductComponent } from './page-product/page-product.component';
import { ProductGalleryComponent } from './page-product/product-gallery/product-gallery.component';
import { PageCustomerComponent } from './page-customer/page-customer.component';
import { PriceAndAddCartComponent } from './page-product/price-and-add-cart/price-and-add-cart.component';
import { CustomerNavComponent } from './page-customer/customer-nav/customer-nav.component';
import { CustomerInfoComponent } from './page-customer/customer-info/customer-info.component';
import {HttpClientModule} from "@angular/common/http";
import { ModalRegComponent } from './header/nav-customer-button/modal-reg/modal-reg.component';
import {FormsModule} from "@angular/forms";


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
    ModalRegComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
