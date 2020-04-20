import {Component, OnInit} from '@angular/core';
import {CustomerInfo, CustomerService} from '../customer.service';
import {Auth} from '../auth';

@Component({
  selector: 'app-page-customer',
  templateUrl: './page-customer.component.html',
  styleUrls: ['./page-customer.component.css']
})
export class PageCustomerComponent implements OnInit {
  customerInfo: CustomerInfo;

  constructor(private customerService: CustomerService, private auth: Auth) {
  }

  ngOnInit(): void {
    this.getCustomerInfo();
  }

  getCustomerInfo() {
    this.customerService.getCustomerInfo().subscribe(info => {
      this.customerInfo = info;
      console.log(this.customerInfo);
    });
  }
}
