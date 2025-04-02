# Bridging High-Fidelity Simulations and Physics-Based Learning Using A Surrogate Model for Soft Robot Control


## 📂 Data Availability

The `Dataset/` folder contains structured data used for training surrogate models, evaluating pressure mappings, and validating simulation outputs. Below is a brief description of each file:

| File Name                            | Description |
|-------------------------------------|-------------|
| **ForwardDynamics_Pybullet_joint_to_position.csv** | Maps joint-level commands to end-effector positions using PyBullet forward dynamics. The end-effector positions are matched with the FEM data and corresponding pressure inputs and external force applied|
| **MotionCaptureData_ROM.csv**       | Captured real-world motion trajectories used to build reduced-order models (ROM). |
| **Pressure_vs_TCP.csv**             | Shows the relationship between internal pressure inputs and the resulting TCP (Tool Center Point) position. Used in surrogate modeling. |
| **PressureThetaMappingData.csv**    | Maps pressure values to internal angular deformations (θ). Supports internal ROM training. |
| **RealPressure_vs_SOFAPressure.csv**| Compares real sensor pressures to simulated pressures in SOFA for calibration and validation. |
| **SOFA_snapshot_data.csv**          | Captured nodal displacement and deformation data from SOFA simulations. Supports sensor modeling and FEM validation. |
| **SurrogateModel_ROM.csv**          | Pretrained ROM dataset for surrogate model input-output mapping. Useful for fast inference and control learning. |
| **SurrogateModel_withTooltip_ROM.csv** | Same as above, but includes tooltip-related deformations or outputs. For tasks involving tool contact or manipulation. |

All files are in `.csv` format and can be opened with any standard spreadsheet or numerical computing tool. They are designed to support both analytical modeling and data-driven learning methods.

