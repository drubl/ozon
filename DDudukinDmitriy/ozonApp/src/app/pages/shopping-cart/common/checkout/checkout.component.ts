import {Component, Input, OnInit} from '@angular/core';
import {CheckOutData} from "../../../../UsersCart";
import {CartService} from "../../../../services/cart.service";

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {
  @Input() checkOut: CheckOutData;
  constructor() { }
  ngOnInit(): void {
  }
}
