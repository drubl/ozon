import {Component, Input, OnInit} from '@angular/core';
import {Cart} from '../../services/cart.service';
import {AuthService} from '../../../../core/auth/auth.service';

@Component({
  selector: 'app-information-products',
  templateUrl: './information-products.component.html',
  styleUrls: ['./information-products.component.css']
})
export class InformationProductsComponent implements OnInit {
  @Input() cart: Cart;
  constructor(private auth: AuthService) { }
  ngOnInit(): void {
  }
}
