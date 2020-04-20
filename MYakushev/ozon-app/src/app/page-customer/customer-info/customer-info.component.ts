import {Component, Input, OnInit} from '@angular/core';
import {CustomerInfo, CustomerService} from '../../customer.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-customer-info',
  templateUrl: './customer-info.component.html',
  styleUrls: ['./customer-info.component.css']
})
export class CustomerInfoComponent implements OnInit {
  @Input() customerInfo: CustomerInfo;
  changeMailToggle = true;
  changePhoneToggle = true;
  changeFioToggle = true;
  changeDateToggle = true;
  changeGenderToggle = true;
  newMail: string;
  newPhone: string;
  newFio: string;
  newDate: string;
  newGender: string;



  constructor(private customerService: CustomerService, private router: Router) { }

  ngOnInit(): void {
  }

  changeMail() {
    this.changeMailToggle = !this.changeMailToggle;
  }
  saveMail() {
    this.changeMailToggle = !this.changeMailToggle;
    this.customerInfo.email = this.newMail;
    this.customerService.sendNewMail(this.newMail).subscribe();
  }

  changePhone() {
    this.changePhoneToggle = !this.changePhoneToggle;
  }
  savePhone() {
    this.changePhoneToggle = !this.changePhoneToggle;
    this.customerInfo.phone = this.newPhone;
    this.customerService.sendNewPhone(this.newPhone).subscribe();
  }

  changeFio() {
    this.changeFioToggle = !this.changeFioToggle;
  }
  saveFio() {
    this.changeFioToggle = !this.changeFioToggle;
    this.customerInfo.name = this.newFio;
    this.customerService.sendNewFio(this.newFio).subscribe();
  }

  changeDate() {
    this.changeDateToggle = !this.changeDateToggle;
  }
  saveDate() {
    this.changeDateToggle = !this.changeDateToggle;
    this.customerInfo.birthday = this.newDate;
    this.customerService.sendNewDate(this.newDate).subscribe();
  }

  changeGender() {
    this.changeGenderToggle = !this.changeGenderToggle;
  }
  saveGender() {
    this.changeGenderToggle = !this.changeGenderToggle;
    this.customerInfo.gender = this.newGender;
    this.customerService.sendNewGender(this.newGender).subscribe();
  }

  deleteProfile() {
    this.customerService.deleteProfile().subscribe(answer => {
      this.router.navigate(['/search']);
      window.location.reload();
    });
  }
}
