import { MatDialogModule } from '@angular/material/dialog';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { SearchFormComponent } from './header/common/search-form/search-form.component';
import { ProductCardComponent } from './product-card/product-card.component';
import { ProfilePageComponent } from './pages/profile-page/profile-page.component';
import { ProductInformationComponent } from './pages/product-information/product-information.component';
import { ProfileSideBarComponent } from './pages/profile-page/common/profile-side-bar/profile-side-bar.component';
import { ShoppingCartComponent } from './pages/shopping-cart/shopping-cart.component';
import { SearchPageComponent } from './pages/search-page/search-page.component';
import { ShoppingCartProductComponent } from './pages/shopping-cart/common/shopping-cart-product/shopping-cart-product.component';
import { CheckoutComponent } from './pages/shopping-cart/common/checkout/checkout.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { ModalComponent } from './header/common/modal/modal.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RegisterComponent } from './header/common/modal/register/register.component';
import { AuthenticateComponent } from './header/common/modal/authenticate/authenticate.component';
import { EntranceComponent } from './header/common/modal/entrance/entrance.component';
import {CookieService} from "ngx-cookie-service";
import { HomePageComponent } from './pages/home-page/home-page.component';
import { CategorySideBarComponent } from './pages/home-page/common/category-side-bar/category-side-bar.component';
import { ModalCategoryComponent } from './header/common/modal/category/modal-category.component';
import { CategoryItemComponent } from './category-item/category-item.component';

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
    CheckoutComponent,
    ModalComponent,
    RegisterComponent,
    AuthenticateComponent,
    EntranceComponent,
    HomePageComponent,
    CategorySideBarComponent,
    ModalCategoryComponent,
    CategoryItemComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatDialogModule
  ],
  providers: [CookieService],
  bootstrap: [AppComponent],
  entryComponents: [ModalComponent]
})
export class AppModule { }
