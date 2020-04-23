import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {ProductService} from '../../pages/page-product/services/product.service';
import {AuthLoginData, AuthService} from '../../core/auth/auth.service';
import {CookieService} from 'ngx-cookie-service';
import {Router} from '@angular/router';
import {CartService} from '../../pages/page-cart/services/cart.service';
import {AuthRegData} from './modal-window/pages/modal-page-reg/modal-page-reg.component';

@Component({
  selector: 'app-nav-customer-button',
  templateUrl: './nav-customer-button.component.html',
  styleUrls: ['./nav-customer-button.component.css']
})
export class NavCustomerButtonComponent {
  @Output() onClickLogOut: EventEmitter<string> = new EventEmitter<string>();
  @Output() onClickLogIn: EventEmitter<AuthLoginData> = new EventEmitter<AuthLoginData>();
  @Output() onClickReg: EventEmitter<AuthRegData> = new EventEmitter<AuthRegData>();

  toggleShowWindowModal = false;
  toggleShowPageModal = true;

  constructor(private productService: ProductService,
              public auth: AuthService,
              private cookieService: CookieService,
              private router: Router,
              private cardService: CartService) {
  }

  registration($event: AuthRegData) {
    this.auth.registration($event).subscribe();
  }

  clickLogOutButton() {
    this.onClickLogOut.emit();
  }

  clickLogInButton($event: AuthLoginData) {
    this.onClickLogIn.emit($event);
  }

  clickRegistrationButton($event: AuthRegData) {
    this.onClickReg.emit($event);
  }
}
