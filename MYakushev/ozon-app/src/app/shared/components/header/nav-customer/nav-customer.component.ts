import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav-customer',
  templateUrl: './nav-customer.component.html',
  styleUrls: ['./nav-customer.component.scss']
})
export class NavCustomerComponent implements OnInit {
  toggleModalLogin = false;
  toggleModalCustomer = false;
  toggleModalCart = false;
  displayNoneSignIn = false;

  constructor() { }

  ngOnInit() {
  }

  eventMouseEnterModalLogin() {
    this.toggleModalLogin = true;
  }
  eventMouseLeaveModalLogin(event) {
    if (!(event.toElement.className.includes('modal-login'))) {
      this.toggleModalLogin = false;
    }
  }

  eventMouseEnterModalCustomer() {
    this.toggleModalCustomer = true;
  }
  eventMouseLeaveModalCustomer(event) {
    if (!(event.toElement.className.includes('modal-customer'))) {
      this.toggleModalCustomer = false;
    }
  }

  eventMouseEnterModalCart() {
    this.toggleModalCart = true;
  }
  eventMouseLeaveModalCart(event) {
    if (!(event.toElement.className.includes('modal-cart'))) {
      this.toggleModalCart = false;
    }
  }

  showModalReg() {
    this.displayNoneSignIn = true;
  }

  showModalLogin() {
    this.displayNoneSignIn = false;
  }
}
