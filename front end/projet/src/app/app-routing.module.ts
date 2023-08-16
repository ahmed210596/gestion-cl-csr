import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AddProductsComponent} from './add-products/add-products.component';
import { AddUsersComponent } from './add-users/add-users.component';
import { BoardAdminComponent } from './board-admin/board-admin.component';
import { BoardModeratorComponent } from './board-moderator/board-moderator.component';


import { EditProductsComponent } from './edit-products/edit-products.component';
import { EditUsersComponent } from './edit-users/edit-users.component';
import { HomeComponent } from './home/home.component';
import { ListProductsComponent } from './list-products/list-products.component';
import { ListUsersComponent } from './list-users/list-users.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { SignupComponent } from './signup/signup.component';
import { AuthGuardService } from './auth-guard.service';
import { UpdateProfileComponent } from './update-profile/update-profile.component';
import { PasswordResetFormComponent } from './password-reset-form/password-reset-form.component';
import { PasswordresetComponent } from './passwordreset/passwordreset.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { ChangePasswordComponent } from './change-password/change-password.component';
import { ListSerialsComponent } from './list-serials/list-serials.component';
import { AddSerialsComponent } from './add-serials/add-serials.component';
import { EditSerialsComponent } from './edit-serials/edit-serials.component';
import { AddCsrComponent } from './add-csr/add-csr.component';
import { EditCsrComponent } from './edit-csr/edit-csr.component';
import { KeyCSRListComponent } from './key-csr-list/key-csr-list.component';
const routes: Routes = [{path:'list-users',component:ListUsersComponent,canActivate: [AuthGuardService]},
{path:'edit/:id',component:EditUsersComponent,canActivate: [AuthGuardService]},
{path:'add-user',component:AddUsersComponent,canActivate: [AuthGuardService]},
{path:'add-prod',component:AddProductsComponent,canActivate: [AuthGuardService]},
{path:'prod/:id',component:EditProductsComponent,canActivate: [AuthGuardService]},
{path:'list-prod',component:ListProductsComponent,canActivate: [AuthGuardService]},
{path:'list-serial',component:ListSerialsComponent,canActivate: [AuthGuardService]},
{path:'add-serial',component:AddSerialsComponent,canActivate: [AuthGuardService]},
{path:'edit-serial/:id',component:EditSerialsComponent,canActivate: [AuthGuardService]},
{path:'add-csr',component:AddCsrComponent,canActivate: [AuthGuardService]},
{path:'edit-csr/:id',component:EditCsrComponent,canActivate: [AuthGuardService]},
{path:'list-csr',component:KeyCSRListComponent,canActivate: [AuthGuardService]},

{ path: 'login', component: LoginComponent },
{path : '', component:LoginComponent},
{ path: 'signup', component: SignupComponent},
{ path: 'home', component: HomeComponent,canActivate: [AuthGuardService] },

{path:'reset-password/:uidb64/:token',component:ResetPasswordComponent},
{path:'send-email',component:PasswordResetFormComponent},
{path:'reset-password',component:PasswordresetComponent},


{ path: 'mod', component: BoardModeratorComponent ,canActivate: [AuthGuardService]},
{ path: 'admin', component: BoardAdminComponent ,canActivate: [AuthGuardService]},

{ path: 'profile', component: ProfileComponent ,canActivate: [AuthGuardService]},
{ path: 'update-profile/:id', component: UpdateProfileComponent ,canActivate: [AuthGuardService]},
{ path: 'change-password', component: ChangePasswordComponent ,canActivate: [AuthGuardService]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
