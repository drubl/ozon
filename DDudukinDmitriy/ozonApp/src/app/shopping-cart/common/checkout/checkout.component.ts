import {Component, Input, OnInit} from '@angular/core';
import {UsersCart} from "../../../UsersCart";
import {CartService} from "../../../services/cart.service";

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {
@Input() shoppingCartProduct: UsersCart
  constructor(private cartService: CartService) { }
  checkOut: any;
  ngOnInit(): void {
  this.checkOutData()
  }
  checkOutData(){
    this.cartService.getUserCart()
      .subscribe(data => {
        this.checkOut = data;
        console.log(this.checkOut)
      })
  }
}
