import {Component, Input, OnInit} from '@angular/core';
import {CustomerInfo} from '../../customer.service';

@Component({
  selector: 'app-customer-nav',
  templateUrl: './customer-nav.component.html',
  styleUrls: ['./customer-nav.component.css']
})
export class CustomerNavComponent implements OnInit {
  @Input() customerInfo: CustomerInfo;
  constructor() { }

  ngOnInit(): void {
  }

}
