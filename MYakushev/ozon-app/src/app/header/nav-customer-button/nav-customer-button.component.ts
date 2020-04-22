import { Component, OnInit } from '@angular/core';
import {ProductService} from '../../product.service';
import {Observable, of} from 'rxjs';
import {Auth} from "../../auth";
import {CookieService} from 'ngx-cookie-service';
import {Router} from '@angular/router';
import {CartService} from '../../cart.service';

@Component({
  selector: 'app-nav-customer-button',
  templateUrl: './nav-customer-button.component.html',
  styleUrls: ['./nav-customer-button.component.css']
})
export class NavCustomerButtonComponent implements OnInit {
  toggleModal = true;
  public countProducts: number;
  private token = this.cookieService.get('csrftoken');
  constructor(private productService: ProductService, public auth: Auth, private cookieService: CookieService, private router: Router, private cardService: CartService) {
  }
  ngOnInit(): void {
    this.cardService.getProductsCart().subscribe(answer => {
      this.countProducts = answer.countProducts;
    });
  }

  authLogout() {
    this.auth.logout().subscribe(anwser => {
      console.log(anwser);
      this.router.navigate(['/search']);
      window.location.reload();
    });
  }
}
